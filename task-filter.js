
function getCompletedTaskTitles(tasks) {
    return tasks
      .filter(task => task.status === 'completed')
      .sort((a, b) => a.id - b.id)
      .map(task => task.title);
  }
  
  // Przykład użycia
  const tasks = [
    { id: 3, title: 'Napisać dokumentację', status: 'completed' },
    { id: 1, title: 'Przygotować projekt', status: 'completed' },
    { id: 4, title: 'Przetestować aplikację', status: 'pending' },
    { id: 2, title: 'Napisać kod', status: 'completed' }
  ];
  
  console.log(getCompletedTaskTitles(tasks));
  