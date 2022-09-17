meaning = '''
                <div class="container">
                    <h2></h2>'''
                                  
     
example_template='''
                <div class="container">
                    <h2></h2>'''
    
closing ='''
                </div>
                <hr>
                <br>'''
                                
word='''
                <div class="container">
                    <h2></h2>'''
                    
nav='''
        <nav class="navbar bg-light">
            <div class="container-fluid">
                <span class="navbar-brand mb-0 h1">Dascal</span>
                <img src="../res/icon.ico" alt="Bootstrap" width="30" height="24">
            </div>
        </nav>'''
        
head='''
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Bootstrap demo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
            <script>
      function printFunction() { 
        window.print(); 
      }
    </script>
        </head>'''


headings = {
    "english":['Word','Meanings','Synonym',"Example Sentences",'Read More','Download PDF'],
    "русский":['Слово','Значения','Синонимы','Примеры предложений','Читать далее',"Скачать PDF"],
    "deutsch":['Wort','Bedeutungen','Synonyme','Beispielsätze','Weiterlesen','Herunterladen PDF']
}      
def make(lang,title,li,example,read_more_url):
    
    if len(li)<2:
        synonym = ''
        closing2 = ''
        li.append('')
    else:
        synonym ='''
                <div class="container">
                    <h2></h2>'''
        closing2=closing

    template =f'''
    <html>
        {head}
        <body>
            {nav}
            <div class="container">
                <br>
                {word.replace('</h2>',f'{headings[lang.lower()][0]}</h2>')}      
                    {title}
                {closing}
                
                {meaning.replace('</h2>',f'{headings[lang.lower()][1]}</h2>')}
                    {li[0]}
                {closing}
                
                {synonym.replace('</h2>',f'{headings[lang.lower()][2]}</h2>')}
                    {li[1]}
                {closing2}
                
                {example_template.replace('</h2>',f'{headings[lang.lower()][3]}</h2>')}
                    {example}
                {closing}
                
                <div class="d-grid gap-2 col-6 mx-auto">
                    <button class="btn btn-primary" type="button" onclick="location.href = '{read_more_url}';">{headings[lang.lower()][4]}</button>
                    <button class="btn btn-primary" type="button" onclick="printFunction()">{headings[lang.lower()][5]}</button>
                </div>
            </div>
            <br><br><br>
        </body>
    </html>'''
        
    return template
        