// Controlled browser-contract checks. No satellite or participant observations.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const zlib = require("node:zlib");
const { test } = require("node:test");
const html = fs.readFileSync("src/app/assets/index_hover/index.html", "utf8");
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];

function context() {
  const elements = {};
  const ctx = vm.createContext({
    window: { parent: { postMessage() {} }, addEventListener() {} },
    document: { getElementById(id) { return elements[id] ??= { style: {}, textContent: "" }; } },
    console, Blob, Response, DecompressionStream, Uint8Array, Float32Array,
    atob, requestAnimationFrame(fn) { fn(); },
    proj4: Object.assign((src, dst, coords) => coords, { defs: () => true }),
  });
  vm.runInContext(script, ctx);
  return { ctx, elements };
}

test("legend uses the supplied negative range, including its midpoint", () => {
  const { ctx } = context();
  vm.runInContext(`args={index_name:"NDWI",palette:["white","blue"],range:[-0.6,-0.1]};
    var container={}; legend={getContainer:()=>container}; updateLegend();`, ctx);
  const legend = vm.runInContext("container.innerHTML", ctx);
  assert.match(legend, /-0.600/);
  assert.match(legend, /-0.350/);
  assert.match(legend, /-0.100/);
});

test("cursor and tap lookup numeric cells and reject bounds/NoData", () => {
  const { ctx, elements } = context();
  vm.runInContext(`
    args={index_name:"NDVI",value_grid:{crs:"EPSG:32622",
      transform:[10,0,0,0,-10,20],first_column:0,first_row:0,nodata:-9999}};
    loadedGrids={NDVI:{rows:1,columns:2,data:new Float32Array([0.42,-9999])}};
    showLocalValue({latlng:{lng:5,lat:15}});
  `, ctx);
  assert.equal(elements["pixel-tooltip"].textContent, "NDVI: 0.4200");
  vm.runInContext("showLocalValue({latlng:{lng:15,lat:15}})", ctx);
  assert.equal(elements["pixel-tooltip"].textContent, "Sem dado");
  vm.runInContext("showLocalValue({latlng:{lng:100,lat:15}})", ctx);
  assert.equal(elements["pixel-tooltip"].textContent, "Sem dado");
  assert.match(script, /map\.on\("click", onMouseMove\)/);
});

test("zlib/Base64 transfer decodes into float32 without remote calls", async () => {
  const { ctx } = context();
  const bytes = Buffer.alloc(8);
  bytes.writeFloatLE(-0.2, 0); bytes.writeFloatLE(0.8, 4);
  ctx.encoded = zlib.deflateSync(bytes).toString("base64");
  const grid = await vm.runInContext("decodeGrid(encoded)", ctx);
  assert.ok(Math.abs(grid[0] + 0.2) < 1e-6);
  assert.ok(Math.abs(grid[1] - 0.8) < 1e-6);
});
