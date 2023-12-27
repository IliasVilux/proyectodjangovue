<script>
    export let data;
    let dni = data.id ? data.id : '';
</script>

<form method="POST" action={data.id ? "?/update" : "?/create"}>
    <input type="text" name="dni" bind:value={dni} />
    <input type="text" name="name" value={data.title ? data.title : ''}>

    {#if !data.id}
        <button type="submit" disabled={dni.length < 1}>Crear</button>
    {:else}
        <button type="submit">Modificar</button>
    {/if}
</form>