# DB2ADMIN.PROJECTBUDGETDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `PROJECTCOMPANYCODE`, `PROJECTCODE`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `BUDGETUSERGRPUSERGENGRPTYPECOD`, `BUDGETUSERGRPCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190585

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PROJECTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROJECTCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 15 | `BUDGETUSERGRPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `BUDGETAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 17 | `ADDBUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `BUDGETBEFOREPLANNINGRUN` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROJECTBUDGETDETAIL.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PROJECTBUDGETDETAIL.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PROJECT_DETAIL` | `PROJECTCOMPANYCODE`, `PROJECTCODE` | [`PROJECT`](../CORE_MASTER/PROJECT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROJECTBUDGETDETAIL.PROJECTCOMPANYCODE = PROJECT.COMPANYCODE AND PROJECTBUDGETDETAIL.PROJECTCODE = PROJECT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROJECTBUDGETDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PROJECTCOMPANYCODE,
       t.PROJECTCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.PROJECTBUDGETDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
