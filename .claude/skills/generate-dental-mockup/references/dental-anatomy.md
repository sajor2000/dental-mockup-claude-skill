# Dental anatomy and esthetic prompt translation

Use these rules to translate terse clinician instructions into an image-editing prompt. Do not use them to select treatment or override the clinician's requested scope.

## Tooth numbering

Interpret `#N` and `#N-M` as the Universal permanent-tooth system unless the clinician explicitly names another system. Ask when notation is genuinely ambiguous; numbering-system confusion can cause wrong-tooth errors.

Maxillary teeth relevant to `#3-14`, from the patient's right to left:

| Tooth | Anatomy |
|---|---|
| #3 | Maxillary right first molar |
| #4 | Maxillary right second premolar |
| #5 | Maxillary right first premolar |
| #6 | Maxillary right canine |
| #7 | Maxillary right lateral incisor |
| #8 | Maxillary right central incisor |
| #9 | Maxillary left central incisor |
| #10 | Maxillary left lateral incisor |
| #11 | Maxillary left canine |
| #12 | Maxillary left first premolar |
| #13 | Maxillary left second premolar |
| #14 | Maxillary left first molar |

`#3-14` therefore spans the maxillary first molar on one side through the maxillary first molar on the other, not just the six anterior teeth. The maxillary dental midline is the contact between #8 and #9. The mandibular dental midline is the contact between #24 and #25.

## Translate common instructions

- **“Line up midlines top and bottom”**: align the maxillary midline (#8/#9), mandibular midline (#24/#25), and visible facial midline. Keep the occlusal plane believable and do not create a jaw shift or duplicate teeth.
- **“Improve shade”**: improve value/lightness first, then harmonize chroma and hue. Preserve a natural cervical-to-incisal gradient, incisal translucency/opalescence, surface texture, and small tooth-to-tooth variation. Avoid flat, opaque, uniformly white “piano key” teeth.
- **“Improve symmetry”**: match contralateral tooth classes in position, width, length, axial inclination, gingival contour, and visible embrasures while retaining natural, patient-specific variation. Do not mirror-copy one side.
- **“Replace missing tooth”**: restore the tooth at the existing edentulous site with the correct tooth class, orientation, dimensions, contact points, and shade based on the contralateral tooth and adjacent space. Do not add a supernumerary tooth. If the site is not visually unambiguous, ask for the tooth number.
- **“Veneers #3-14”**: treat this as a clinician-directed appearance scope. Apply a coherent veneer-style facial restorative result to the visible portions of Universal teeth #3 through #14, including the named molars and premolars. Do not reinterpret it as #6-11. If a tooth in the range is missing, restore the missing tooth first, then harmonize its visible form and shade with the requested range.

## Anatomy and image-editing guardrails

- Preserve the patient's identity, facial proportions, head pose, lips, skin, hair, expression, camera perspective, lighting, and background unless explicitly asked otherwise.
- Edit the dentition and immediately adjacent visible gingiva only. Do not change unrelated anatomy.
- Preserve tooth order and tooth count except for the explicitly requested replacement of a missing tooth. Avoid fused, duplicated, floating, or extra teeth.
- Keep tooth-specific morphology: central incisors visually dominant; lateral incisors slightly smaller; canines form the anterior-posterior transition; premolars and molars retain posterior crown form.
- Maintain a natural smile arc: the maxillary incisal curve should relate coherently to the lower-lip curvature rather than becoming unnaturally flat.
- Maintain believable gingival scallop and papillae. When compatible with the observed anatomy, maxillary central-incisor zeniths sit slightly distal to the tooth long axis, lateral-incisor margins are slightly more coronal, and canine zeniths are near the long axis. Do not force textbook measurements onto diseased, recessed, or otherwise patient-specific gingiva.
- Avoid introducing open gingival embrasures or “black triangles” unless they are present and the clinician asks to preserve them.
- Treat the photograph as a visualization. Do not claim the rendering is technically achievable or an expected clinical result.

## Example expansion

Original request:

> Full aesthetic upgrade. Line up midlines top and bottom. Improve shade. Improve symmetry. Replace missing tooth. Veneers #3-14.

Expanded image-editing prompt:

> Create a photorealistic dental concept edit of the supplied patient photograph. Preserve the patient's identity, face, lips, expression, head position, skin, lighting, camera perspective, and background. Edit only the teeth and immediately adjacent visible gingiva. Use the Universal tooth-numbering system. Align the maxillary dental midline at the #8/#9 contact with the mandibular midline at the #24/#25 contact and the visible facial midline, while keeping the occlusal plane and jaw relationship believable. Restore the single visibly missing tooth at its existing anatomic site using the correct tooth class and dimensions derived from the contralateral tooth and adjacent space; do not add any extra teeth. Apply a coherent veneer-style facial restorative appearance to the visible portions of maxillary teeth #3 through #14: right first molar, right premolars, right canine and incisors, left incisors and canine, left premolars, and left first molar. Improve bilateral harmony of tooth position, width, length, axial inclination, gingival contours, contacts, and embrasures without producing mechanically mirrored or identical teeth. Improve shade naturally by increasing value and harmonizing chroma and hue while preserving cervical warmth, incisal translucency/opalescence, surface texture, and subtle tooth-to-tooth variation; avoid opaque uniform white teeth. Maintain tooth-specific morphology, a natural smile arc related to the lower lip, believable gingival scallop and papillae, and the correct tooth order and count. Do not alter lower teeth beyond the requested midline relationship. Produce a realistic concept preview, not a guaranteed treatment outcome.

## PubMed grounding

- Smile analysis integrates facial esthetics, lip dynamics, gingival (“pink”) esthetics, dental (“white”) esthetics, and patient-specific characteristics: [Sabbah, 2022, PMID 35738730](https://pubmed.ncbi.nlm.nih.gov/35738730/).
- Digital smile design and mockups can support dentist-patient-technician communication, but photographic simulation has limitations and should be confirmed clinically: [Garcia et al., 2018, PMID 30122831](https://pubmed.ncbi.nlm.nih.gov/30122831/).
- Restorative esthetics proceeds through position, contour, texture, and color; dental color includes value, chroma, hue, and translucency: [Sikri, 2010, PMID 21217954](https://pubmed.ncbi.nlm.nih.gov/21217954/).
- The smile arc relates the curvature of the maxillary incisal edges to the lower-lip curvature and is affected by posture and photographic angle: [Seixas and Câmara, 2021, PMID 34231836](https://pubmed.ncbi.nlm.nih.gov/34231836/).
- Published maxillary-anterior reference data describe tooth-specific gingival-zenith patterns rather than a single uniform gingival line: [Chu et al., 2009, PMID 19368601](https://pubmed.ncbi.nlm.nih.gov/19368601/).
- Open gingival embrasures and altered gingival characteristics materially affect perceived smile esthetics: [Alomari et al., 2022, PMID 34520516](https://pubmed.ncbi.nlm.nih.gov/34520516/).
- Color, translucency, and whiteness differences have perceptibility and acceptability thresholds; a mockup should not imply exact clinical shade reproduction: [Paravina et al., 2019, PMID 30891913](https://pubmed.ncbi.nlm.nih.gov/30891913/).
- Universal, FDI, and Palmer/Zsigmondy notation coexist, making explicit numbering interpretation important: [Kannan and Gurunathan, 2016, PMID 27723633](https://pubmed.ncbi.nlm.nih.gov/27723633/).
