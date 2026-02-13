def verificador_media(media:int|float) ->str:
    """Esta função retorna se o aluno passou ou nao  de ano"""

    if media >= 7:
        return "Aprovado(a)"
    elif media <= 5:
        return "Reprovado(a)"
    else:
        return "Recuperação"
    
if __name__ =="__main__":
    print(verificador_media(7))