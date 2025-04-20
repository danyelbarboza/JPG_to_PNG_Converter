# Conversor JPG para PNG

## Descrição
Ferramenta para conversão de imagens JPG/JPEG para formato PNG com opções de redimensionamento. Desenvolvido em Python com interface Tkinter e biblioteca Pillow para processamento de imagens.

## Funcionalidades Principais
### Conversão de Imagens
- Suporte a arquivos JPG e JPEG
- Conversão para PNG com preservação de qualidade
- Processamento em lote de diretórios inteiros

### Controle de Tamanho
- Redimensionamento proporcional (50%, 100%, 200%)
- Algoritmo LANCZOS para alta qualidade no redimensionamento
- Opções pré-definidas com feedback visual

### Interface
- Seleção gráfica de pastas de origem e destino
- Área de log detalhada para acompanhamento
- Botões de tamanho com estado visual claro

## Requisitos Técnicos
- Python 3.x
- Biblioteca Pillow (PIL Fork)
- Tkinter (incluído na instalação padrão do Python)

Instalação das dependências:
pip install pillow


## Como Utilizar
1. Execute o aplicativo: python jpg_to_png_converter.py

2. Selecione a pasta de origem contendo imagens JPG/JPEG

3. Escolha a pasta de destino para os arquivos PNG

4. Selecione o fator de redimensionamento:
   - 50% para reduzir pela metade
   - 100% para manter tamanho original
   - 200% para dobrar o tamanho

5. Clique em "Iniciar Conversão"

6. Acompanhe o progresso na área de status


## Licença
MIT License - Disponível para uso e modificação. Consulte o arquivo LICENSE para detalhes.

--------------------------------------

# JPG to PNG Converter

## Description
Tool for converting JPG/JPEG images to PNG format with resizing options. Developed in Python with Tkinter interface and Pillow library for image processing.

## Key Features
### Image Conversion
- Supports JPG and JPEG files
- Conversion to PNG with quality preservation
- Batch processing of entire directories

### Size Control
- Proportional resizing (50%, 100%, 200%)
- LANCZOS algorithm for high-quality resizing
- Predefined options with visual feedback

### Interface
- Graphical selection of source and destination folders
- Detailed log area for monitoring
- Size buttons with clear visual state

## Technical Requirements
- Python 3.x
- Pillow library (PIL Fork)
- Tkinter (included in standard Python installation)

Install dependencies:
pip install pillow

## How to Use
1. Run the application: python jpg_to_png_converter.py

2. Select source folder containing JPG/JPEG images

3. Choose destination folder for PNG files

4. Select resize factor:
   - 50% to halve the size
   - 100% for original size
   - 200% to double the size

5. Click "Start Conversion"

6. Monitor progress in the status area

## License
MIT License - Available for use and modification. See LICENSE file for details.