# DB2ADMIN.FINASYNCCLEARING

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `INTERNALCLEARINGNBR`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99559

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `INTERNALCLEARINGNBR` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 3 | `INTERNALSEQUENCENBR` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 4 | `INTERNALVOUCHERMASTER` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 5 | `VOUCHERLINE` | DECIMAL(5,0) |  |  |  |  |
| 6 | `SUBLINE` | DECIMAL(5,0) |  |  |  |  |
| 7 | `PROCESSINGSTATUS` | CHAR(2) |  |  |  |  |
| 8 | `ONLYPOSTING` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINASYNCCLEARING.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINASYNCCLEARINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INTERNALCLEARINGNBR,
       t.INTERNALSEQUENCENBR,
       t.INTERNALVOUCHERMASTER,
       t.VOUCHERLINE,
       t.SUBLINE,
       t.PROCESSINGSTATUS,
       t.ONLYPOSTING,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.FINASYNCCLEARING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
