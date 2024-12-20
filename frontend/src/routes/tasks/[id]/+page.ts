import type { Load } from "@sveltejs/kit";

export const load:Load = async (event) => {
    const { id } = event.params;

    const res = await fetch(`http://127.0.0.1:8000/tasks/${id}`);
    
    if (!res.ok) {
        throw new Error('Failed to fetch task');
    }

    const responseBody = await res.json();

    console.log(responseBody); 
    return {
        id:id,
        title: responseBody.title,
        description: responseBody.description,  
        deadline: responseBody.deadline,
        completed: responseBody.completed
    };
};
