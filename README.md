# LRD Schematic Figure Quiz

A CSV-driven schematic-figure quiz for Little Red Dot (LRD) papers, designed to run on GitHub Pages and embed cleanly in Google Sites.

## Repository structure

```text
lrd-schematic-quiz/
├─ index.html
├─ data/
│  ├─ papers.csv      # one row per paper
│  ├─ figures.csv     # one row per schematic figure
│  └─ audit.csv       # candidate figures not yet added to the quiz
├─ assets/
│  └─ figures/        # add your PNG/JPG/WebP files here
├─ scripts/
│  └─ validate_data.py
└─ .nojekyll
```

The public web page intentionally shows only the quiz. Maintenance notes, the audit list, and image-management instructions remain in the repository rather than appearing on the quiz page.

## Add a figure

### 1. Put the image in `assets/figures/`

Example:

```text
assets/figures/naidu2026_mom_bhstar_fig3.png
```

Use ASCII-only filenames when possible.

### 2. Add the paper to `data/papers.csv`

Skip this step if the paper is already present.

```csv
paper_id,authors,year,title,arxiv,source_url,notes
naidu26-mom,Naidu et al.,2026,A gas-enshrouded and gas-reddened black hole at cosmic dawn,,https://www.nature.com/articles/s41586-026-10846-4,
```

Recommended convention: use the arXiv identifier as `paper_id` when one exists.

### 3. Add the schematic figure to `data/figures.csv`

```csv
figure_id,paper_id,figure_label,image_path,remote_image_url,description,enabled
naidu26-fig3,naidu26,Figure 3,assets/figures/naidu2026_mom_bhstar_fig3.png,,Gas-enshrouded black-hole schematic,1
```

Columns:

- `figure_id`: unique ID for the schematic figure.
- `paper_id`: must match a row in `papers.csv`.
- `figure_label`: e.g. `Figure 1`, `Figure 3`, or `Schematic A`.
- `image_path`: local image path inside this repository. This is tried first.
- `remote_image_url`: optional direct image URL used as a fallback.
- `description`: short explanation shown after the answer is revealed.
- `enabled`: `1` to include the figure in the quiz; `0` to temporarily exclude it.

If one paper contains multiple independent schematic figures, keep one row in `papers.csv` and add multiple rows to `figures.csv`.

## Suggested workflow for your own figures

For papers such as Naidu+, Chen+, de Graaff+, Inayoshi+, etc.:

1. Export or crop the schematic figure as PNG/JPG/WebP.
2. Add it to `assets/figures/`.
3. Add or update the paper metadata in `papers.csv`.
4. Add one row per figure in `figures.csv`.
5. Run the validator.
6. Commit and push to GitHub.

No edits to `index.html` are needed when adding ordinary quiz questions.

## Validate the CSV files

From the repository root:

```bash
python scripts/validate_data.py
```

The script checks for duplicate IDs, unknown `paper_id` references, enabled figures without an image source, and missing local image files.

## Preview locally

Because `index.html` loads the CSV files with `fetch()`, do not test it by double-clicking the HTML file.

Run a local server instead:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

## Publish with GitHub Pages

1. Upload the contents of this folder to the root of a GitHub repository.
2. Open **Settings → Pages** in the repository.
3. Choose **Deploy from a branch**.
4. Select `main` and `/ (root)`.
5. Save and wait for the GitHub Pages URL to appear.

## Embed in Google Sites

1. In Google Sites, choose **Insert → Embed**.
2. Select **By URL**.
3. Paste the GitHub Pages URL for the quiz.
4. Resize the embedded frame to give the figure enough vertical space.

## Existing data

The current deck contains 33 schematic figures from 30 papers, including locally stored figures from Inayoshi+, Chen+, de Graaff+, and Naidu+ supplied for this project. The collection is managed entirely through `papers.csv` and `figures.csv`. Many entries currently use a `remote_image_url`. As you add your own image files, populate `image_path`; the quiz will try the local file first and fall back to the remote URL if needed.

`data/audit.csv` contains candidate schematic figures that were identified but not yet added as active quiz questions. It is for maintenance only and is not shown on the public quiz page.

## Copyright and figure permissions

A public GitHub Pages repository redistributes any image files that you upload to it. Before publishing paper figures in `assets/figures/`, check the applicable article license and publisher permissions. If redistribution is not permitted or is unclear, keeping only a remote source URL may be preferable.
