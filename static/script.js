function resolverRuta() {
    const resultado = document.getElementById('resultado');
    resultado.innerHTML = "<p>Calculando la mejor ruta...</p>";
  
    fetch('/tsp')
      .then(response => response.json())
      .then(data => {
        const rutaHTML = data.mejor_ruta.map(ciudad => `<span>${ciudad}</span>`).join(" → ");
        resultado.innerHTML = `
          <p><strong>Mejor Ruta:</strong><br>${rutaHTML}</p>
          <p><strong>Distancia Total:</strong> <span>${data.distancia_total}</span> unidades</p>
        `;
      })
      .catch(error => {
        resultado.innerHTML = "<p>Error al calcular la ruta.</p>";
        console.error('Error:', error);
      });
  }
  