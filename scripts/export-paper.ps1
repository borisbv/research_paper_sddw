param(
    [ValidateSet("docx", "pdf", "all")]
    [string]$Format = "all",

    [string]$OutputBaseName = "paper"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$PaperDir = Join-Path $RepoRoot "paper"
$SectionsDir = Join-Path $PaperDir "sections"
$MetadataFile = Join-Path $PaperDir "metadata.yaml"
$BibliographyFile = Join-Path $RepoRoot "references\references.bib"

$SectionFiles = @(
    "abstract.md",
    "introduction.md",
    "marco-teorico.md",
    "methodology.md",
    "results.md",
    "discussion.md",
    "conclusion.md"
) | ForEach-Object { Join-Path $SectionsDir $_ }

function Assert-CommandExists {
    param(
        [Parameter(Mandatory = $true)]
        [string]$CommandName,

        [string]$InstallHint = ""
    )

    if (-not (Get-Command $CommandName -ErrorAction SilentlyContinue)) {
        $message = "No se encontró el comando requerido: $CommandName"
        if ($InstallHint) {
            $message += ". $InstallHint"
        }
        throw $message
    }
}

function Assert-PathExists {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PathToCheck
    )

    if (-not (Test-Path -LiteralPath $PathToCheck)) {
        throw "No se encontró el archivo requerido: $PathToCheck"
    }
}

Assert-CommandExists -CommandName "pandoc" -InstallHint "Instala Pandoc y vuelve a ejecutar este script."
Assert-PathExists -PathToCheck $MetadataFile
Assert-PathExists -PathToCheck $BibliographyFile
$SectionFiles | ForEach-Object { Assert-PathExists -PathToCheck $_ }

$CommonArgs = @(
    "--metadata-file=$MetadataFile",
    "--bibliography=$BibliographyFile",
    "--citeproc",
    "--from=markdown+yaml_metadata_block",
    "--resource-path=$RepoRoot"
) + $SectionFiles

function Invoke-PandocExport {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet("docx", "pdf")]
        [string]$TargetFormat
    )

    $OutputFile = Join-Path $PaperDir "$OutputBaseName.$TargetFormat"
    $Args = @($CommonArgs)

    if ($TargetFormat -eq "docx") {
        $Args += @(
            "--to=docx",
            "--output=$OutputFile"
        )
    }
    else {
        Assert-CommandExists -CommandName "xelatex" -InstallHint "Instala TeX Live o MiKTeX para exportar a PDF."
        $Args += @(
            "--pdf-engine=xelatex",
            "--output=$OutputFile"
        )
    }

    Write-Host "Generando $TargetFormat -> $OutputFile"
    & pandoc @Args

    if ($LASTEXITCODE -ne 0) {
        throw "Pandoc terminó con código $LASTEXITCODE al generar $TargetFormat."
    }
}

switch ($Format) {
    "docx" { Invoke-PandocExport -TargetFormat "docx" }
    "pdf" { Invoke-PandocExport -TargetFormat "pdf" }
    "all" {
        Invoke-PandocExport -TargetFormat "docx"
        Invoke-PandocExport -TargetFormat "pdf"
    }
}

Write-Host "Exportación completada."
