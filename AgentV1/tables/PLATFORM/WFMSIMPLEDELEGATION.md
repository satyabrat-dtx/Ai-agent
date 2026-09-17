# DB2ADMIN.WFMSIMPLEDELEGATION

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `USERIDUSERID`, `COMPANYCODE`, `PROCESSPROCESSID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189920

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 1 | `USERIDUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PROCESSPROCESSID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `INITIALDATE` | DATE |  |  |  |  |
| 5 | `FINALDATE` | DATE |  |  |  |  |
| 6 | `DELEGATETOUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_DELEGATETO` | `DELEGATETOUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `WFMSIMPLEDELEGATION.DELEGATETOUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_USERID` | `USERIDUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `WFMSIMPLEDELEGATION.USERIDUSERID = ABSUSERDEF.USERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WFMSIMPLEDELEGATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENABLED,
       t.USERIDUSERID,
       t.COMPANYCODE,
       t.PROCESSPROCESSID,
       t.INITIALDATE,
       t.FINALDATE,
       t.DELEGATETOUSERID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.WFMSIMPLEDELEGATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
