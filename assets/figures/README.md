# Figure images

Put your quiz images in this folder. Example:

```text
assets/figures/naidu_2026_fig3.png
assets/figures/degraaff_2025_fig1.jpg
assets/figures/inayoshi_2024_fig2.png
```

Then set the corresponding `image_path` in `data/figures.csv`, for example:

```csv
naidu26-fig3,naidu26,Figure 3,assets/figures/naidu_2026_fig3.png,,Gas-enshrouded BH schematic,1
```

`image_path` takes priority over `remote_image_url`. Keep filenames ASCII-only when possible.
