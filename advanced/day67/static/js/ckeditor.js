// CKEditor 5 Full Configuration
const {
    ClassicEditor,
    Essentials,
    Bold,
    Italic,
    Underline,
    Strikethrough,
    Font,
    FontSize,
    FontFamily,
    FontColor,
    FontBackgroundColor,
    Paragraph,
    Heading,
    Link,
    List,
    BlockQuote,
    Indent,
    IndentBlock,
    Alignment,
    Image,
    ImageToolbar,
    ImageCaption,
    ImageStyle,
    ImageResize,
    LinkImage,
    Table,
    TableToolbar,
    MediaEmbed,
    Code,
    CodeBlock,
    HorizontalLine,
    RemoveFormat,
    SourceEditing
} = CKEDITOR;

function initCKEditor(selector) {
    ClassicEditor
        .create(document.querySelector(selector), {
            plugins: [
                Essentials, Bold, Italic, Underline, Strikethrough,
                Font, FontSize, FontFamily, FontColor, FontBackgroundColor,
                Paragraph, Heading, Link, List, BlockQuote,
                Indent, IndentBlock, Alignment,
                Image, ImageToolbar, ImageCaption, ImageStyle, ImageResize, LinkImage,
                Table, TableToolbar, MediaEmbed,
                Code, CodeBlock, HorizontalLine, RemoveFormat, SourceEditing
            ],
            toolbar: {
                items: [
                    'sourceEditing', '|',
                    'heading', '|',
                    'bold', 'italic', 'underline', 'strikethrough', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
                    'link', 'insertImage', 'insertTable', 'mediaEmbed', '|',
                    'bulletedList', 'numberedList', '|',
                    'alignment', 'outdent', 'indent', '|',
                    'blockQuote', 'code', 'codeBlock', 'horizontalLine', '|',
                    'removeFormat', '|',
                    'undo', 'redo'
                ],
                shouldNotGroupWhenFull: true
            },
            heading: {
                options: [
                    { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
                    { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
                    { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },
                    { model: 'heading3', view: 'h3', title: 'Heading 3', class: 'ck-heading_heading3' },
                    { model: 'heading4', view: 'h4', title: 'Heading 4', class: 'ck-heading_heading4' }
                ]
            },
            image: {
                toolbar: ['imageStyle:inline', 'imageStyle:block', 'imageStyle:side', '|', 'toggleImageCaption', 'imageTextAlternative', '|', 'linkImage']
            },
            table: {
                contentToolbar: ['tableColumn', 'tableRow', 'mergeTableCells']
            }
        })
        .catch(error => {
            console.error('CKEditor initialization error:', error);
        });
}