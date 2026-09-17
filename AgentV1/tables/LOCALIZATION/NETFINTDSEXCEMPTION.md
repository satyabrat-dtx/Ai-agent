# DB2ADMIN.NETFINTDSEXCEMPTION

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `PANNO`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222398

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PANNO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 6 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 7 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `NETFINTDSEXCEMPTION_LINE` | [`NETFINTDSEXCEMPTIONDETAIL`](../LOCALIZATION/NETFINTDSEXCEMPTIONDETAIL.md) | `NETFINTDSEXCEMPTIONCOMPANYCODE`, `NETFINTDSEXCEMPTIONPANNO` | `NETFINTDSEXCEMPTIONDETAIL.NETFINTDSEXCEMPTIONCOMPANYCODE = NETFINTDSEXCEMPTION.COMPANYCODE AND NETFINTDSEXCEMPTIONDETAIL.NETFINTDSEXCEMPTIONPANNO = NETFINTDSEXCEMPTION.PANNO` |

## Indexes

- `NETFINTDSEXCEMPTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PANNO,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NETFINTDSEXCEMPTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
