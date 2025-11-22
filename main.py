import flet as ft
import conexao as db

def main(page: ft.Page):
    page.title = "Estoque SENAI"

    titulo_field = ft.TextField(label="Nome do produto")
    preco_field = ft.TextField(label="Preco", keyboard_type="number")
    lista_produtos = ft.ListView(expand=True, spacing=10)

    def carregar_dados():
        lista_produtos.controls.clear()  # limpa a lista
        for id_p, titulo, preco in db.ler_produtos():
            lista_produtos.controls.append(
                ft.ListTile(
                    title=ft.Text(titulo),
                    subtitle=ft.Text(f"R$ {preco:.2f}"),
                    trailing=ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_color="red",
                        data=id_p,
                        on_click=deletar_item
                    )
                )
            )

        page.update()  # atualiza a interface


    def salvar_item(e):
        db.inserir_produto(titulo_field.value, float(preco_field.value))
        titulo_field.value = ""
        preco_field.value = ""
        carregar_dados()
        titulo_field.focus()
        page.update()

    def deletar_item(e):
        id_produto = e.control.data
        db.deletar_produtos(id_produto)
        carregar_dados()

    btn_salvar = ft.ElevatedButton("Salvar", on_click=salvar_item)

    page.add(
        ft.Text("Sistema de estoque", size=24),
        titulo_field, preco_field, btn_salvar,
        ft.Divider(),
        lista_produtos
    )
    carregar_dados()
ft.app(target=main)