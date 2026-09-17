# DB2ADMIN.LOGASSETCUSTOMIZEDOPTIONS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 22
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 100594

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CHECKDEPRECIATIONTYPECODE` | CHAR(20) |  |  |  |  |
| 2 | `ASSETMASTERFIRSTUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 3 | `ASSETMASTERFIRSTUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 4 | `ASSETMASTERSNDUSERGRPCMYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ASSETMASTERSECONDUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `ASSETMASTERTHIRDUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 7 | `ASSETMASTERTHIRDUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 8 | `ASSETMASTERFOURTHUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 9 | `ASSETMASTERFOURTHUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 10 | `ASSETMASTERFIFTHUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 11 | `ASSETMASTERFIFTHUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 18 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 19 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 20 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 21 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGASSETCUSTOMIZEDOPTIONS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CHECKDEPRECIATIONTYPECODE,
       t.ASSETMASTERFIRSTUSERGRPCMYCOD,
       t.ASSETMASTERFIRSTUSERGROUPCODE,
       t.ASSETMASTERSNDUSERGRPCMYCODE,
       t.ASSETMASTERSECONDUSERGROUPCODE,
       t.ASSETMASTERTHIRDUSERGRPCMYCOD,
       t.ASSETMASTERTHIRDUSERGROUPCODE,
       t.ASSETMASTERFOURTHUSERGRPCMYCOD,
       t.ASSETMASTERFOURTHUSERGROUPCODE,
       t.ASSETMASTERFIFTHUSERGRPCMYCOD,
       t.ASSETMASTERFIFTHUSERGROUPCODE
FROM   DB2ADMIN.LOGASSETCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
