<!-- <script>
    export let data;
    const colaborador = {
        dniCifColaborador: '',
        nombreColaborador: ''
    }

    $: {
        colaborador.dniCifColaborador = data.dniCifColaborador || colaborador.dniCifColaborador;
        colaborador.nombreColaborador = data.nombreColaborador || colaborador.nombreColaborador;
    }

    async function handleSubmit(){
        console.log(colaborador)
    }
</script>

<form method="POST" on:submit|preventDefault={handleSubmit}>
    <input type="text" name="dni" bind:value={colaborador.dniCifColaborador} />
    <input type="text" name="name" value={colaborador.nombreColaborador ? colaborador.nombreColaborador : ''}>

    {#if !data.dniCifColaborador}
        <button type="submit" disabled={colaborador.dniCifColaborador.length < 1}>Crear</button>
    {:else}
        <button type="submit">Modificar</button>
    {/if}
</form> -->

<script>
</script>
