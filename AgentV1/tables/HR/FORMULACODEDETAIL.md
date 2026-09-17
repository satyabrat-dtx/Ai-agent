# DB2ADMIN.FORMULACODEDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `FORMULACODECOMPANYCODE`, `FORMULACODECODE`, `SERIALNUMBER`, `RESULTVARIABLE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 153301

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FORMULACODECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FORMULACODECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SERIALNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `RESULTVARIABLE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `OPERATOR1TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `OPERATORVARIABLE1C` | CHAR(10) |  |  |  |  |
| 6 | `OPERATORVARIABLE1N` | DECIMAL(11,4) |  |  |  |  |
| 7 | `OPERATORVARIABLE1RPELEMENTTE` | CHAR(1) |  | FK | foreign_key |  |
| 8 | `OPERATORVARIABLE1RCODE` | CHAR(6) |  | FK | foreign_key |  |
| 9 | `OPERATOR2TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `OPERATORVARIABLE2C` | CHAR(10) |  |  |  |  |
| 11 | `OPERATORVARIABLE2N` | DECIMAL(11,4) |  |  |  |  |
| 12 | `OPERATORVARIABLE2RPELEMENTTE` | CHAR(1) |  | FK | foreign_key |  |
| 13 | `OPERATORVARIABLE2RCODE` | CHAR(6) |  | FK | foreign_key |  |
| 14 | `OPERATOR` | INTEGER | NOT NULL |  |  |  |
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
| `FORMULACODE_LINE` | `FORMULACODECOMPANYCODE`, `FORMULACODECODE` | [`FORMULACODE`](../HR/FORMULACODE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FORMULACODEDETAIL.FORMULACODECOMPANYCODE = FORMULACODE.COMPANYCODE AND FORMULACODEDETAIL.FORMULACODECODE = FORMULACODE.CODE` |
| `PAYELEMENT_OPERATORVARIABLE1R` | `FORMULACODECOMPANYCODE`, `OPERATORVARIABLE1RPELEMENTTE`, `OPERATORVARIABLE1RCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `FORMULACODEDETAIL.FORMULACODECOMPANYCODE = PAYELEMENT.COMPANYCODE AND FORMULACODEDETAIL.OPERATORVARIABLE1RPELEMENTTE = PAYELEMENT.PAYELEMENTTYPE AND FORMULACODEDETAIL.OPERATORVARIABLE1RCODE = PAYELEMENT.CODE` |
| `PAYELEMENT_OPERATORVARIABLE2R` | `FORMULACODECOMPANYCODE`, `OPERATORVARIABLE2RPELEMENTTE`, `OPERATORVARIABLE2RCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `FORMULACODEDETAIL.FORMULACODECOMPANYCODE = PAYELEMENT.COMPANYCODE AND FORMULACODEDETAIL.OPERATORVARIABLE2RPELEMENTTE = PAYELEMENT.PAYELEMENTTYPE AND FORMULACODEDETAIL.OPERATORVARIABLE2RCODE = PAYELEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FORMULACODEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FORMULACODECOMPANYCODE,
       t.FORMULACODECODE,
       t.SERIALNUMBER,
       t.RESULTVARIABLE,
       t.OPERATOR1TYPE,
       t.OPERATORVARIABLE1C,
       t.OPERATORVARIABLE1N,
       t.OPERATORVARIABLE1RPELEMENTTE,
       t.OPERATORVARIABLE1RCODE,
       t.OPERATOR2TYPE,
       t.OPERATORVARIABLE2C,
       t.OPERATORVARIABLE2N
FROM   DB2ADMIN.FORMULACODEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
