const fetchQuestionById = async (questionId) => {
    const query = `
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                content
                difficulty
                codeSnippets {
                    lang
                    code
                }
                stats
            }
        }
    `;

    const variables = {
        titleSlug: questionId
    };

    try {
        const response = await fetch('https://leetcode.com/graphql', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Include any necessary authentication headers
                'Cookie': 'REDACTED', // Replace with your session cookie if required
            },
            body: JSON.stringify({
                query,
                variables
            })
        });

        const data = await response.json();

        if (data.errors) {
            console.error('Errors:', data.errors);
            return null;
        }

        const question = data.data.question;

        if (!question) {
            console.error('No question found with the given ID');
            return null;
        }

        return question;
    } catch (error) {
        console.error('Error fetching question:', error);
        return null;
    }
};

// Example usage:
const questionId = 'two-sum'; // Replace with the desired question ID (slug)
fetchQuestionById(questionId).then(question => {
    if (question) {
        console.log('Question Details:', question);
    }
});