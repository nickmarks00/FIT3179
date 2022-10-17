const vg1 = "./src/js/energy-cons-map.vg.json";
vegaEmbed("#cons-map", vg1, { actions: false })
  .then((result) => {})
  .catch(console.error);

const vg2 = "./src/js/energy-cons-change-map.vg.json";
vegaEmbed("#cons-map-change", vg2, { actions: false })
  .then((result) => {})
  .catch(console.error);

const vg4 = "./src/js/parallel-usage.vg.json";
vegaEmbed("#parallel-plot", vg4, { actions: false })
  .then((res) => {})
  .catch(console.error);
