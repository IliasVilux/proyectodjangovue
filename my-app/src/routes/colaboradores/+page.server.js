// Here goes the request of "colaboradores" data using GraphQL

export async function load() {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    const colaboradores_json = await response.json()
    
	return {
		colaboradores: colaboradores_json.map((post) => ({
			dni: post.id,
			title: post.title
		}))
	};
}