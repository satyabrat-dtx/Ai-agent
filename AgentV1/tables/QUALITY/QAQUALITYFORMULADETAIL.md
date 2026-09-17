# DB2ADMIN.QAQUALITYFORMULADETAIL

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `QAQUALITYFORMULACOMPANYCODE`, `QAQUALITYFORMULACODE`, `SEQUENCE`, `RESULTVARIABLE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192887

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QAQUALITYFORMULACOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `QAQUALITYFORMULACODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `RESULTVARIABLE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `OPERATOR1TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `OPERATOR1VARIABLE` | CHAR(10) |  |  |  |  |
| 6 | `OPERATORVARIABLE1C` | CHAR(10) |  |  |  |  |
| 7 | `OPERATORVARIABLE1N` | DECIMAL(18,5) |  |  |  |  |
| 8 | `OPERATORVARIABLE1RCODE` | CHAR(10) |  | FK | foreign_key |  |
| 9 | `OPERATOR` | INTEGER | NOT NULL |  |  |  |
| 10 | `OPERATOR2TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `OPERATOR2VARIABLE` | CHAR(10) |  |  |  |  |
| 12 | `OPERATORVARIABLE2C` | CHAR(10) |  |  |  |  |
| 13 | `OPERATORVARIABLE2N` | DECIMAL(18,5) |  |  |  |  |
| 14 | `OPERATORVARIABLE2RCODE` | CHAR(10) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `STEP` | CHAR(1) |  |  |  |  |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `QAQUALITYFORMULA_LINE` | `QAQUALITYFORMULACOMPANYCODE`, `QAQUALITYFORMULACODE` | [`QAQUALITYFORMULA`](../QUALITY/QAQUALITYFORMULA.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAQUALITYFORMULADETAIL.QAQUALITYFORMULACOMPANYCODE = QAQUALITYFORMULA.COMPANYCODE AND QAQUALITYFORMULADETAIL.QAQUALITYFORMULACODE = QAQUALITYFORMULA.CODE` |
| `QUALITYCHARACTERISTICTYPE_OPERATORVARIABLE1R` | `QAQUALITYFORMULACOMPANYCODE`, `OPERATORVARIABLE1RCODE` | [`QUALITYCHARACTERISTICTYPE`](../QUALITY/QUALITYCHARACTERISTICTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAQUALITYFORMULADETAIL.QAQUALITYFORMULACOMPANYCODE = QUALITYCHARACTERISTICTYPE.COMPANYCODE AND QAQUALITYFORMULADETAIL.OPERATORVARIABLE1RCODE = QUALITYCHARACTERISTICTYPE.CODE` |
| `QUALITYCHARACTERISTICTYPE_OPERATORVARIABLE2R` | `QAQUALITYFORMULACOMPANYCODE`, `OPERATORVARIABLE2RCODE` | [`QUALITYCHARACTERISTICTYPE`](../QUALITY/QUALITYCHARACTERISTICTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAQUALITYFORMULADETAIL.QAQUALITYFORMULACOMPANYCODE = QUALITYCHARACTERISTICTYPE.COMPANYCODE AND QAQUALITYFORMULADETAIL.OPERATORVARIABLE2RCODE = QUALITYCHARACTERISTICTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QAQUALITYFORMULADETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.QAQUALITYFORMULACOMPANYCODE,
       t.QAQUALITYFORMULACODE,
       t.SEQUENCE,
       t.RESULTVARIABLE,
       t.OPERATOR1TYPE,
       t.OPERATOR1VARIABLE,
       t.OPERATORVARIABLE1C,
       t.OPERATORVARIABLE1N,
       t.OPERATORVARIABLE1RCODE,
       t.OPERATOR,
       t.OPERATOR2TYPE,
       t.OPERATOR2VARIABLE
FROM   DB2ADMIN.QAQUALITYFORMULADETAIL t
FETCH FIRST 100 ROWS ONLY;
```
