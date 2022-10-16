const vg1 = "./src/js/energy-cons-country.vg.json";
vegaEmbed("#cons-country", vg1)
  .then((result) => {})
  .catch(console.error);

const vg2 = "./src/js/energy-cons-map.vg.json";
vegaEmbed("#cons-map", vg2)
  .then((result) => {})
  .catch(console.error);

const vg3 = "./src/js/energy-cons-change-map.vg.json";
vegaEmbed("#cons-change-map", vg3)
  .then((res) => {})
  .catch(console.error);

const vg4 = "./src/js/parallel-usage.vg.json";
vegaEmbed("#parallel-plot", vg4)
  .then((res) => {})
  .catch(console.error);
