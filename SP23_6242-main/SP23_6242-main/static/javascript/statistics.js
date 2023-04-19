google.charts.load("current", { packages: ["corechart"] });

const number_of_passwords_generated = document.getElementById(
  "number-of-passwords-generated"
);
const max_passwords_generated = document.getElementById(
  "max-passwords-generated"
);
const average_passwords_generated = document.getElementById(
  "average-passwords-generated"
);
const average_password_length = document.getElementById(
  "average_password_length"
);
const min_symbols = document.getElementById("min_symbols");

google.charts.setOnLoadCallback(async () => {
  const stats = await fetch("/api/statistics_submission").then((res) =>
    res.json()
  );

  number_of_passwords_generated.innerText = stats.length;
  max_passwords_generated.innerText = stats.reduce(
    (prev, x) =>
      parseInt(x.number_of_passwords) > prev
        ? parseInt(x.number_of_passwords)
        : prev,
    0
  );
  average_passwords_generated.innerText =
    stats.reduce((prev, x) => prev + parseInt(x.number_of_passwords), 0) /
    stats.length;

  average_password_length.innerText =
    stats.reduce((prev, x) => prev + parseInt(x.password_length), 0) /
    stats.length;

  min_symbols.innerText = stats.reduce(
    (prev, x) =>
      parseInt(x.min_symbols) < prev ? parseInt(x.min_symbols) : prev,
    Infinity
  );

  let data = new google.visualization.DataTable();
  data.addColumn("string", "Password Type");
  data.addColumn("number", "Amount");

  data.addRows([
    [
      "Simple",
      stats.filter(({ password_type }) => password_type == "Simple").length,
    ],
    [
      "Moderate",
      stats.filter(({ password_type }) => password_type == "Moderate").length,
    ],
    [
      "Complex",
      stats.filter(({ password_type }) => password_type == "Complex").length,
    ],
  ]);

  const chart = new google.visualization.PieChart(
    document.getElementById("stats_chart")
  );

  chart.draw(data, {
    title: "Password Types Requested",
    width: 222,
    height: 196,
  });
});
