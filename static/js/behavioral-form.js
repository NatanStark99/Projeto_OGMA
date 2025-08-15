        // Progress bar update
        function updateProgress() {
            const form = document.getElementById('behavioralForm');
            const totalQuestions = 10;
            const personalDataFields = ['nome', 'cargo', 'empresa', 'departamento'];
            const questionFields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'];
            
            let completedPersonalData = 0;
            let completedQuestions = 0;
            
            // Check personal data
            personalDataFields.forEach(field => {
                const input = form.elements[field];
                if (input && input.value.trim() !== '') {
                    completedPersonalData++;
                }
            });
            
            // Check questions
            questionFields.forEach(field => {
                const inputs = form.elements[field];
                if (inputs && inputs.value) {
                    completedQuestions++;
                }
            });
            
            const totalFields = personalDataFields.length + totalQuestions;
            const completedFields = completedPersonalData + completedQuestions;
            const progress = (completedFields / totalFields) * 100;
            
            document.getElementById('progressFill').style.width = progress + '%';
        }

        // Add event listeners to all form elements
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('behavioralForm');
            
            // Listen to all input changes
            form.addEventListener('input', updateProgress);
            form.addEventListener('change', updateProgress);
            
            // Initial progress update
            updateProgress();
        });

        // Form submission
        document.getElementById('behavioralForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Calculate behavioral scores
            const scores = {
                adaptabilidade: (parseInt(data.q1) + parseInt(data.q7)) / 2,
                colaboracao: (parseInt(data.q2) + parseInt(data.q3)) / 2,
                resolucaoProblemas: (parseInt(data.q4) + parseInt(data.q8)) / 2,
                gestaoEstresse: parseInt(data.q5),
                comunicacao: parseInt(data.q6),
                receptividadeFeedback: parseInt(data.q9),
                organizacao: parseInt(data.q10)
            };
            
            // Display results
            let resultsText = `Avaliação completa para ${data.nome}!\n\n`;
            resultsText += `Cargo: ${data.cargo}\n`;
            resultsText += `Empresa: ${data.empresa}\n`;
            resultsText += `Departamento: ${data.departamento}\n\n`;
            resultsText += `Pontuações Comportamentais:\n`;
            resultsText += `• Adaptabilidade: ${scores.adaptabilidade.toFixed(1)}/5\n`;
            resultsText += `• Colaboração: ${scores.colaboracao.toFixed(1)}/5\n`;
            resultsText += `• Resolução de Problemas: ${scores.resolucaoProblemas.toFixed(1)}/5\n`;
            resultsText += `• Gestão de Estresse: ${scores.gestaoEstresse}/5\n`;
            resultsText += `• Comunicação: ${scores.comunicacao}/5\n`;
            resultsText += `• Receptividade a Feedback: ${scores.receptividadeFeedback}/5\n`;
            resultsText += `• Organização: ${scores.organizacao}/5\n`;
            
            alert(resultsText);
            
            // Here you would typically send the data to your server
            console.log('Form Data:', data);
            console.log('Behavioral Scores:', scores);
        });