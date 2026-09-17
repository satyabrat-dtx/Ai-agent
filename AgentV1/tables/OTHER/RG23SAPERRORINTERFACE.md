# DB2ADMIN.RG23SAPERRORINTERFACE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `PLANTCODE`, `POSTINGTYPECODE`, `RG23MONTH`, `RG23TYPE`, `CODE`, `COUNTER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 143696

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `POSTINGTYPECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `RG23MONTH` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `RG23TYPE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COUNTER` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `FLAG` | CHAR(15) |  |  |  |  |
| 10 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RG23SAPERRORINTERFACE.COMPANYCODE = COMPANY.CODE` |
| `EVENTMASTER_POSTINGTYPE` | `POSTINGTYPECODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `RG23SAPERRORINTERFACE.POSTINGTYPECODE = EVENTMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG23SAPERRORINTERFACEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.POSTINGTYPECODE,
       t.RG23MONTH,
       t.RG23TYPE,
       t.CODE,
       t.COUNTER,
       t.FLAG,
       t.SAPMESSAGE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.RG23SAPERRORINTERFACE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
