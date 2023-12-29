<script>
</script>

<nav>
    <a href="/">Home</a> |
    <a href="/colaboradores">Colaboradores</a>
</nav>

<slot />

<style>
    nav{
        background-color: #0B1215;
        padding: 20px;
        color: white;
    }

    :global(a){
        text-decoration: none;
        color: #0B1215;
    }
    a{
        color: white;
    }
</style>