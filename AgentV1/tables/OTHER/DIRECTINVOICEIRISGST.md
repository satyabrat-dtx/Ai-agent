# DB2ADMIN.DIRECTINVOICEIRISGST

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221842

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `BOOKINGFOR` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `DOCUMENT` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `TYPEFOREINVOICE` | CHAR(1) |  |  |  |  |
| 8 | `STATUS` | CHAR(100) |  |  |  |  |
| 9 | `EINVOICEQRCODE` | LONG VARCHAR |  |  |  |  |
| 10 | `ACKNO` | BIGINT | NOT NULL |  |  |  |
| 11 | `ACKDT` | CHAR(29) |  |  |  |  |
| 12 | `IRN` | CHAR(160) |  |  |  |  |
| 13 | `SIGNEDQRCODE` | LONG VARCHAR |  |  |  |  |
| 14 | `EWBNO` | CHAR(120) |  |  |  |  |
| 15 | `EWBDT` | CHAR(29) |  |  |  |  |
| 16 | `EWBVALIDTILL` | VARCHAR(1000) |  |  |  |  |
| 17 | `CANCLEDATE` | CHAR(100) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DIRECTINVOICEIRISGST.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIRECTINVOICEIRISGST.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND DIRECTINVOICEIRISGST.COUNTERCODE = COUNTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIRECTINVOICEIRISGSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.BOOKINGFOR,
       t.DOCUMENT,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.TYPEFOREINVOICE,
       t.STATUS,
       t.EINVOICEQRCODE,
       t.ACKNO,
       t.ACKDT
FROM   DB2ADMIN.DIRECTINVOICEIRISGST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
