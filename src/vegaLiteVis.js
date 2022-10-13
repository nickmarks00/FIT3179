const vg1 = "vg/energy-cons-country.vg.json";
vegaEmbed("#cons-country", vg1)
  .then((result) => {})
  .catch(console.error);

const vg2 = "vg/energy-cons-map.vg.json";
vegaEmbed("#cons-map", vg2)
  .then((result) => {})
  .catch(console.error);
