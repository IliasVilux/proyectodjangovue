<script>
	import { ApolloClient, InMemoryCache } from '@apollo/client/core';
	import { setClient } from 'svelte-apollo';

	const cache = new InMemoryCache({
		typePolicies: {
			ColaboradorType: {
				keyFields: ['dniCifColaborador']
			}
		}
	});
	const client = new ApolloClient({
		uri: 'http://127.0.0.1:8000/graphql/',
		cache: cache
	});
	setClient(client);
</script>

<nav>
	<a href="/">Home</a> |
	<a href="/colaboradores">Colaboradores</a>
</nav>

<slot />

<style>
	nav {
		background-color: #0b1215;
		padding: 20px;
		color: white;
	}

	:global(a) {
		text-decoration: none;
		color: #0b1215;
	}
	a {
		color: white;
	}
</style>
