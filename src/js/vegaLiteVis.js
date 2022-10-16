const vg1 = "./src/js/energy-cons-country.vg.json";
vegaEmbed("#cons-country", vg1)
  .then((result) => {})
  .catch(console.error);

const vg2 = "./src/js/energy-cons-map.vg.json";
vegaEmbed("#cons-map", vg2)
  .then((result) => {})
  .catch(console.error);
