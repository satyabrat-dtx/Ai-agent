# DB2ADMIN.PRICINGDEFINITIONELEMENTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `PRICINGDEFINITIONCOMPANYCODE`, `PRICINGDEFINITIONNUMBERID`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104929

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRICINGDEFINITIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PRICINGDEFINITIONNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `SIGN` | CHAR(1) |  |  |  |  |
| 7 | `ISMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CONSIDERINSUBSEQ` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CRITERIA` | CHAR(1) |  |  |  |  |
| 10 | `UNITVALUEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRICINGDEFINITION_DEFELEMENTS` | `PRICINGDEFINITIONCOMPANYCODE`, `PRICINGDEFINITIONNUMBERID` | [`PRICINGDEFINITION`](../CORE_MASTER/PRICINGDEFINITION.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `PRICINGDEFINITIONELEMENTS.PRICINGDEFINITIONCOMPANYCODE = PRICINGDEFINITION.COMPANYCODE AND PRICINGDEFINITIONELEMENTS.PRICINGDEFINITIONNUMBERID = PRICINGDEFINITION.NUMBERID` |
| `UNITOFMEASURE_UNITVALUEUOM` | `UNITVALUEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PRICINGDEFINITIONELEMENTS.UNITVALUEUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRICINGDEFINITIONELEMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PRICINGDEFINITIONCOMPANYCODE,
       t.PRICINGDEFINITIONNUMBERID,
       t.SEQUENCE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SIGN,
       t.ISMANDATORY,
       t.CONSIDERINSUBSEQ,
       t.CRITERIA,
       t.UNITVALUEUOMCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRICINGDEFINITIONELEMENTS t
FETCH FIRST 100 ROWS ONLY;
```
