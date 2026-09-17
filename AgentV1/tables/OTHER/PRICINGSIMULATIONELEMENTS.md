# DB2ADMIN.PRICINGSIMULATIONELEMENTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `PRICINGSIMULATIONCOMPANYCODE`, `PRICINGSIMULATIONNUMBERID`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105085

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRICINGSIMULATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PRICINGSIMULATIONNUMBERID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `SIGN` | CHAR(1) |  |  |  |  |
| 7 | `ISMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CONSIDERINSUBSEQ` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CRITERIA` | CHAR(1) |  |  |  |  |
| 10 | `UNITVALUEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `VALUE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CONTRIBUTETOPRICE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRICINGSIMULATION_PRICINGELEMENTS` | `PRICINGSIMULATIONCOMPANYCODE`, `PRICINGSIMULATIONNUMBERID` | [`PRICINGSIMULATION`](../OTHER/PRICINGSIMULATION.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `PRICINGSIMULATIONELEMENTS.PRICINGSIMULATIONCOMPANYCODE = PRICINGSIMULATION.COMPANYCODE AND PRICINGSIMULATIONELEMENTS.PRICINGSIMULATIONNUMBERID = PRICINGSIMULATION.NUMBERID` |
| `UNITOFMEASURE_UNITVALUEUOM` | `UNITVALUEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PRICINGSIMULATIONELEMENTS.UNITVALUEUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRICINGSIMULATIONELEMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PRICINGSIMULATIONCOMPANYCODE,
       t.PRICINGSIMULATIONNUMBERID,
       t.SEQUENCE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SIGN,
       t.ISMANDATORY,
       t.CONSIDERINSUBSEQ,
       t.CRITERIA,
       t.UNITVALUEUOMCODE,
       t.VALUE
FROM   DB2ADMIN.PRICINGSIMULATIONELEMENTS t
FETCH FIRST 100 ROWS ONLY;
```
