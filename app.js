
function CalculadoraRectificado() {
  const [params, setParams] = React.useState({
    diametroMuela: 550,
    anchoMuela: 100,
    rpmMuela: 500,
    diametroCilindro: 619,
    longitudCilindro: 1925,
    avanceZ: 1,
    rpmCilindro: 30,
    relacionQ: 30
  });

  const [resultados, setResultados] = React.useState('');

  const handleChange = (e, param) => {
    setParams({...params, [param]: Number(e.target.value)});
  };

  const calcular = () => {
    const vMuela = (Math.PI * params.diametroMuela * params.rpmMuela) / 60000;
    const vCilindro = (Math.PI * params.diametroCilindro * params.rpmCilindro) / 60000;
    const qReal = vCilindro !== 0 ? vMuela / vCilindro : 0;

    setResultados(`
      Resultados del cálculo:

      1. Velocidad de corte de la muela:
         • Fórmula: v = (π × d × rpm) / 60000
         • Resultado: ${vMuela.toFixed(2)} m/s

      2. Velocidad de corte del cilindro:
         • Fórmula: v = (π × d × rpm) / 60000
         • Resultado: ${vCilindro.toFixed(2)} m/s

      3. Relación Q real:
         • Fórmula: Q = v_muela / v_cilindro
         • Resultado: ${qReal.toFixed(2)}
    `);
  };

  const createNumericInput = (label, param, min, max) => (
    <div className="mb-3">
      <label className="form-label">{label}</label>
      <div className="input-group">
        <button className="btn btn-outline-secondary" onClick={() => setParams({...params, [param]: Math.max(params[param] - 1, min)})}>-</button>
        <input 
          type="number" 
          className="form-control" 
          value={params[param]} 
          onChange={(e) => handleChange(e, param)}
          min={min} 
          max={max}
        />
        <button className="btn btn-outline-secondary" onClick={() => setParams({...params, [param]: Math.min(params[param] + 1, max)})}>+</button>
        <span className="input-group-text">({min}-{max})</span>
      </div>
    </div>
  );

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4">Calculadora Profesional de Rectificado</h1>
      
      <div className="card mb-4">
        <div className="card-header">Parámetros de la Muela</div>
        <div className="card-body">
          {createNumericInput("Diámetro de muela (mm)", "diametroMuela", 550, 915)}
          {createNumericInput("Ancho de muela (mm)", "anchoMuela", 0, 200)}
          {createNumericInput("RPM muela", "rpmMuela", 0, 1000)}
        </div>
      </div>

      <div className="card mb-4">
        <div className="card-header">Parámetros del Cilindro</div>
        <div className="card-body">
          {createNumericInput("Diámetro del cilindro (mm)", "diametroCilindro", 619, 705)}
          {createNumericInput("Longitud del cilindro (mm)", "longitudCilindro", 0, 2000)}
          {createNumericInput("Avance Z (mm/min)", "avanceZ", 0, 100)}
          {createNumericInput("RPM cilindro", "rpmCilindro", 0, 60)}
          {createNumericInput("Relación Q", "relacionQ", 30, 35)}
        </div>
      </div>

      <button className="btn btn-primary mb-4 w-100" onClick={calcular}>Calcular</button>

      <div className="card">
        <div className="card-header">Resultados y Fórmulas</div>
        <div className="card-body">
          <pre>{resultados}</pre>
        </div>
      </div>
    </div>
  );
}

ReactDOM.render(<CalculadoraRectificado />, document.getElementById('root'));
