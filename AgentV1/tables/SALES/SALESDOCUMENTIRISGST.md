# DB2ADMIN.SALESDOCUMENTIRISGST

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `PROVISIONALCODE`, `PROVISIONALCOUNTERCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217243

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `TYPEFOREINVOICE` | CHAR(1) |  |  |  |  |
| 4 | `STATUS` | CHAR(100) |  |  |  |  |
| 5 | `EINVOICEQRCODE` | LONG VARCHAR |  |  |  |  |
| 6 | `ACKNO` | BIGINT | NOT NULL |  |  |  |
| 7 | `ACKDT` | CHAR(29) |  |  |  |  |
| 8 | `IRN` | CHAR(160) |  |  |  |  |
| 9 | `SIGNEDQRCODE` | LONG VARCHAR |  |  |  |  |
| 10 | `EWBNO` | CHAR(120) |  |  |  |  |
| 11 | `EWBDT` | CHAR(29) |  |  |  |  |
| 12 | `EWBVALIDTILL` | VARCHAR(1000) |  |  |  |  |
| 13 | `CANCLEDATE` | CHAR(100) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESDOCUMENTIRISGST.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTIRISGSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.TYPEFOREINVOICE,
       t.STATUS,
       t.EINVOICEQRCODE,
       t.ACKNO,
       t.ACKDT,
       t.IRN,
       t.SIGNEDQRCODE,
       t.EWBNO,
       t.EWBDT
FROM   DB2ADMIN.SALESDOCUMENTIRISGST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
