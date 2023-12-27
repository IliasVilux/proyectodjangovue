<script>
    export let data;
</script>

<div class="container">
    <h1>colaboradores</h1>

    <a href="colaboradores/formulario" class="btn">Agregar Nuevo Colaborador</a>

    {#each data.colaboradores as colaborador}
        <div class="card">
            <a href="colaboradores/{colaborador.dni}">{colaborador.title}</a>
        </div>
    {/each}
</div>

<style>
    .container{
        width: 45%;
        margin: auto;
        text-align: center;
    }
    .card{
        display: flex;
        align-items: center;
        box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
        height: 100px;
        margin: 20px 0;
        vertical-align: middle;
        padding: 10px;
        text-transform: capitalize;
        border-radius: 10px;
    }
    a{
        text-decoration: none;
        color: #333;
    }
    .btn{
        text-align: end;
        background-color: #020D19;
        color: #c5c5c5;
        text-decoration: none;
        padding: 10px;
        border-radius: 20px;
    }
</style>