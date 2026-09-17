# DB2ADMIN.CUSQADOCUMENTDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `CUSQADOCUMENTCOMPANYCODE`, `CUSQADOCUMENTCOUNTERCODE`, `CUSQADOCUMENTCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204474

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSQADOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CUSQADOCUMENTCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CUSQADOCUMENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `MRNDETAILMRNHEADERDIVISIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `MRNDLTMRNHEADERMRNPREFIXCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `MRNDETAILMRNHEADERCODE` | DECIMAL(11,0) |  | FK | foreign_key |  |
| 6 | `MRNDETAILLINEID` | INTEGER | NOT NULL | FK | foreign_key |  |
| 7 | `LINENO` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 8 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 9 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 10 | `PRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 11 | `PRIMARYUOM` | CHAR(3) |  |  |  |  |
| 12 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `DEBITGLCODE` | CHAR(20) |  |  |  |  |
| 14 | `CREDITGLCODE` | CHAR(20) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CUSQADOCUMENT_QADOCUMENTDETAIL` | `CUSQADOCUMENTCOMPANYCODE`, `CUSQADOCUMENTCOUNTERCODE`, `CUSQADOCUMENTCODE` | [`CUSQADOCUMENT`](../OTHER/CUSQADOCUMENT.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `CUSQADOCUMENTDETAIL.CUSQADOCUMENTCOMPANYCODE = CUSQADOCUMENT.COMPANYCODE AND CUSQADOCUMENTDETAIL.CUSQADOCUMENTCOUNTERCODE = CUSQADOCUMENT.COUNTERCODE AND CUSQADOCUMENTDETAIL.CUSQADOCUMENTCODE = CUSQADOCUMENT.CODE` |
| `MRNDETAIL_MRNDETAIL` | `CUSQADOCUMENTCOMPANYCODE`, `MRNDETAILMRNHEADERDIVISIONCODE`, `MRNDLTMRNHEADERMRNPREFIXCODE`, `MRNDETAILMRNHEADERCODE`, `MRNDETAILLINEID` | [`MRNDETAIL`](../CORE_MASTER/MRNDETAIL.md) | `MRNHEADERCOMPANYCODE`, `MRNHEADERDIVISIONCODE`, `MRNHEADERMRNPREFIXCODE`, `MRNHEADERCODE`, `LINEID` | RESTRICT | `CUSQADOCUMENTDETAIL.CUSQADOCUMENTCOMPANYCODE = MRNDETAIL.MRNHEADERCOMPANYCODE AND CUSQADOCUMENTDETAIL.MRNDETAILMRNHEADERDIVISIONCODE = MRNDETAIL.MRNHEADERDIVISIONCODE AND CUSQADOCUMENTDETAIL.MRNDLTMRNHEADERMRNPREFIXCODE = MRNDETAIL.MRNHEADERMRNPREFIXCODE AND CUSQADOCUMENTDETAIL.MRNDETAILMRNHEADERCODE = MRNDETAIL.MRNHEADERCODE AND CUSQADOCUMENTDETAIL.MRNDETAILLINEID = MRNDETAIL.LINEID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CUSQADOCUMENTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CUSQADOCUMENTCOMPANYCODE,
       t.CUSQADOCUMENTCOUNTERCODE,
       t.CUSQADOCUMENTCODE,
       t.MRNDETAILMRNHEADERDIVISIONCODE,
       t.MRNDLTMRNHEADERMRNPREFIXCODE,
       t.MRNDETAILMRNHEADERCODE,
       t.MRNDETAILLINEID,
       t.LINENO,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.PRIMARYQUANTITY,
       t.PRIMARYUOM
FROM   DB2ADMIN.CUSQADOCUMENTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
