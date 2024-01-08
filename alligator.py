from io import StringIO

from cowsay import cattallest , cowthink

cow = cattallest (StringIO("""
$the_cow = <<EOC;
   $thoughts
    $thoughts

      (\\(\\/
  .-._)oo  '_
  \'---.     .\'\\
       )    \\.-\'\\
      /__ ;     (
      |__ : /'._/
       \\_  (
       .,)  )
       \'-.-\'

EOC
"""))
message = """
C'est Mardi matin , le weekend est encore loin !!!
""".strip()
print(cowthink(message, cowfile=cow))

