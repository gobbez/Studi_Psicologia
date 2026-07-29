# Istruzioni per creare nuovi appunti

Questo file contiene le regole per aggiungere nuovi appunti al vault in modo coerente con la struttura esistente.

## Convenzioni generali
- Ogni appunto è un file `.md`.
- Inizia sempre con un **tag tematico** in cima (es. `#psicologia`, `#hce`, `#studi-scientifici`).
- Usa i **link bidirezionali Obsidian** `[[Nome File]]` per collegare gli argomenti tra loro.
- Mantieni un linguaggio **sintetico**: una definizione o una frase iniziale, poi dettagli in elenco puntato.
- I nomi dei file usano le iniziali maiuscole e gli spazi (es. `Influenza Sociale.md`).

---

## Macro-argomento
Un macro-argomento è un contenitore che raggruppa più sotto-argomenti correlati.  
Esempi: `Influenza Sociale`, `Coaching`, `Studi Scientifici`.

1. Crea una **cartella** con il nome del macro-argomento nella root del vault.
2. All'interno della cartella crea un file `Nome Macro.md` con lo **stesso nome** della cartella (es. `Studi Scientifici/Studi Scientifici.md`).
3. Nel file macro inserisci:
   - Un tag tematico in cima.
   - 1-3 frasi di descrizione generale dell'area.
   - Un elenco di link `[[Sotto-argomento]]` agli appunti contenuti.
4. Aggiungi il link `[[Nome Macro]]` nel file `Psicologia.md` (o nel macro di appartenenza superiore).

### Esempio di macro
```markdown
#studi-scientifici

Raccolta di studi empirici e ricerche scientifiche citate nel vault, con sintesi chiare dei metodi e dei risultati.

## [[The Role of Colors in Stress Reduction]]
Cromoterapia blu e rosa per la riduzione dello stress in studenti infermieristici.

[[Psicologia]]
```

---

## Argomento singolo
Un argomento singolo è un concetto, uno studio, una tecnica o una teoria specifica.

1. Crea il file `.md` all'interno della cartella del macro-argomento di riferimento.
2. Scegli un nome breve e significativo (può essere anche il titolo originale dello studio).
3. Nel file inserisci:
   - Un tag tematico in cima.
   - Una sintesi iniziale in 1-2 frasi.
   - Dettagli in elenco puntato.
   - Eventuali link ad altri appunti correlati con `[[...]]`.
4. Se l'argomento rientra in un macro non ancora esistente, crea prima il macro.

### Esempio di argomento singolo
```markdown
#studi-scientifici

# The Role of Colors in Stress Reduction

Studio empirico di Lesley C. Lubos (2008) sul ruolo della cromoterapia nella riduzione dello stress.

## Sintesi
L'esposizione ai colori blu e rosa riduce significativamente il livello di stress in studenti infermieristici dopo il turno ospedaliero.

## Risultati principali
- Il blu si è rivelato più efficace del rosa.
- Il gruppo trattato ha ridotto lo stress più del gruppo di controllo.

## Link
[[Studi Scientifici]]
```

---

## Note finali
- Se il contenuto deriva da un testo, uno studio o un corso specifico, indica autore/anno/fonte in cima.
- Non inserire numeri di pagina o riferimenti troppo formali: l'obiettivo è la sintesi operativa.
- Verifica che i link `[[...]]` puntino a file effettivamente presenti o che si intendono creare.

---

## HCE Questions

Esiste un quiz interattivo, **HCE Questions**, che genera domande a risposta multipla casuali a partire dagli appunti HCE del vault. È hostato su Vercel qui: [https://hcequestions.vercel.app/](https://hcequestions.vercel.app/)

Il file delle domande (`questions.json`) si trova in `Human Connection Enginering (HCE)/website/` e può essere rigenerato in qualsiasi momento eseguendo, dalla stessa cartella:

```bash
python3 generate_questions.py
```

Lo script legge tutti i file `.md` di HCE e delle sue sottocartelle e produce automaticamente le domande con quattro opzioni di risposta.

---

## File "maxi" per cartella

Nella cartella `0_Maximd/` è presente lo script `genera_maxi_md.py`, che genera un file `<Nome Cartella>_maxi.md` per ciascuna cartella principale del vault, concatenando al suo interno tutti i file `.md` trovati ricorsivamente in quella cartella (esclusa la sottocartella `website` di HCE).

Per (ri)generare tutti i file maxi, dalla cartella `0_Maximd/`:

```bash
python genera_maxi_md.py
```

Va rieseguito ogni volta che si aggiungono, modificano o rimuovono appunti, per mantenere i file maxi aggiornati.
