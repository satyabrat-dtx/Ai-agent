# DB2ADMIN.BUDGETITEMSETUPDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `BUDGETCOMPANYCODE`, `BUDGETITEMTYPECODE`, `BUDGETITEMSETUPTYPE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `BUDGETUSERGRPUSERGENGRPTYPECOD`, `BUDGETUSERGRPCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190110

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BUDGETCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BUDGETITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BUDGETITEMSETUPTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 14 | `BUDGETUSERGRPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `EXTRAPERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BUDGETITEMSETUP_DETAIL` | `BUDGETCOMPANYCODE`, `BUDGETITEMTYPECODE`, `BUDGETITEMSETUPTYPE` | [`BUDGETITEMSETUP`](../OTHER/BUDGETITEMSETUP.md) | `COMPANYCODE`, `ITEMTYPECODE`, `TYPE` | RESTRICT | `BUDGETITEMSETUPDETAIL.BUDGETCOMPANYCODE = BUDGETITEMSETUP.COMPANYCODE AND BUDGETITEMSETUPDETAIL.BUDGETITEMTYPECODE = BUDGETITEMSETUP.ITEMTYPECODE AND BUDGETITEMSETUPDETAIL.BUDGETITEMSETUPTYPE = BUDGETITEMSETUP.TYPE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUDGETITEMSETUPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BUDGETCOMPANYCODE,
       t.BUDGETITEMTYPECODE,
       t.BUDGETITEMSETUPTYPE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.BUDGETITEMSETUPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
