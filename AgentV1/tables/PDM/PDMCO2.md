# DB2ADMIN.PDMCO2

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `PDMCO1COMPANYCODE`, `PDMCO1CORECTYCODE`, `PDMCO1COTPREC`, `PDMCO1COCITEM`, `PDMCO1COVERNR`, `PDMCO1COVERST`, `PDMCO1COGRPCO`, `PDMCO1COCDCOL`, `C2CDCOM`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80265

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PDMCO1COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PDMCO1CORECTYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PDMCO1COTPREC` | DECIMAL(1,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PDMCO1COCITEM` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PDMCO1COVERNR` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PDMCO1COVERST` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PDMCO1COGRPCO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `PDMCO1COCDCOL` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `C2CDCOM` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `C2PERCE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PDMCO1_CMP` | `PDMCO1COMPANYCODE`, `PDMCO1CORECTYCODE`, `PDMCO1COTPREC`, `PDMCO1COCITEM`, `PDMCO1COVERNR`, `PDMCO1COVERST`, `PDMCO1COGRPCO`, `PDMCO1COCDCOL` | [`PDMCO1`](../PDM/PDMCO1.md) | `COMPANYCODE`, `CORECTYCODE`, `COTPREC`, `COCITEM`, `COVERNR`, `COVERST`, `COGRPCO`, `COCDCOL` | RESTRICT | `PDMCO2.PDMCO1COMPANYCODE = PDMCO1.COMPANYCODE AND PDMCO2.PDMCO1CORECTYCODE = PDMCO1.CORECTYCODE AND PDMCO2.PDMCO1COTPREC = PDMCO1.COTPREC AND PDMCO2.PDMCO1COCITEM = PDMCO1.COCITEM AND PDMCO2.PDMCO1COVERNR = PDMCO1.COVERNR AND PDMCO2.PDMCO1COVERST = PDMCO1.COVERST AND PDMCO2.PDMCO1COGRPCO = PDMCO1.COGRPCO AND PDMCO2.PDMCO1COCDCOL = PDMCO1.COCDCOL` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMCO2UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PDMCO1COMPANYCODE,
       t.PDMCO1CORECTYCODE,
       t.PDMCO1COTPREC,
       t.PDMCO1COCITEM,
       t.PDMCO1COVERNR,
       t.PDMCO1COVERST,
       t.PDMCO1COGRPCO,
       t.PDMCO1COCDCOL,
       t.C2CDCOM,
       t.C2PERCE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PDMCO2 t
FETCH FIRST 100 ROWS ONLY;
```
