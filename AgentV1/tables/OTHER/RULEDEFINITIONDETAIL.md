# DB2ADMIN.RULEDEFINITIONDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `RULEDEFHEADERCOMPANYCODE`, `RULEDEFINITIONHEADERRULECODE`, `RULEDEFHDRRULECHSKEYSSEQUENCE`, `RULEDEFINITIONHEADERIDENTIFIER`, `RULETEMPLATEDETAILIDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17979

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RULEDEFHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RULEDEFINITIONHEADERRULECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RULEDEFHDRRULECHSKEYSSEQUENCE` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RULEDEFINITIONHEADERIDENTIFIER` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `RULETEMPLATEDETAILIDENTIFIER` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `VALUE` | VARCHAR(100) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RULEDEFINITIONHEADER_VALUESDETAIL` | `RULEDEFHEADERCOMPANYCODE`, `RULEDEFINITIONHEADERRULECODE`, `RULEDEFHDRRULECHSKEYSSEQUENCE`, `RULEDEFINITIONHEADERIDENTIFIER` | [`RULEDEFINITIONHEADER`](../LOCALIZATION/RULEDEFINITIONHEADER.md) | `COMPANYCODE`, `RULECODE`, `RULECHOOSEKEYSSEQUENCE`, `IDENTIFIER` | RESTRICT | `RULEDEFINITIONDETAIL.RULEDEFHEADERCOMPANYCODE = RULEDEFINITIONHEADER.COMPANYCODE AND RULEDEFINITIONDETAIL.RULEDEFINITIONHEADERRULECODE = RULEDEFINITIONHEADER.RULECODE AND RULEDEFINITIONDETAIL.RULEDEFHDRRULECHSKEYSSEQUENCE = RULEDEFINITIONHEADER.RULECHOOSEKEYSSEQUENCE AND RULEDEFINITIONDETAIL.RULEDEFINITIONHEADERIDENTIFIER = RULEDEFINITIONHEADER.IDENTIFIER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RULEDEFDETAIL01` (RULEDEFINITIONHEADERIDENTIFIER, RULEDEFINITIONHEADERRULECODE, RULEDEFHDRRULECHSKEYSSEQUENCE, RULEDEFHEADERCOMPANYCODE, SEQUENCE, VALUE, RULETEMPLATEDETAILIDENTIFIER)
- `RULEDEFINITIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RULEDEFHEADERCOMPANYCODE,
       t.RULEDEFINITIONHEADERRULECODE,
       t.RULEDEFHDRRULECHSKEYSSEQUENCE,
       t.RULEDEFINITIONHEADERIDENTIFIER,
       t.RULETEMPLATEDETAILIDENTIFIER,
       t.VALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.SEQUENCE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RULEDEFINITIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
