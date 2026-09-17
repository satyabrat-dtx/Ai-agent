# DB2ADMIN.USACOMPUTEDSALESTAX

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `DOCUMENTTYPE`, `COUNTERCODE`, `CODE`, `ORDERLINE`, `TAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114745

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DOCUMENTTYPE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `ORDERLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 6 | `TAXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `RATE` | DECIMAL(6,3) |  |  |  |  |
| 8 | `TAXABLEINCOMEINDOCCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TAXABLEINCOMEINCOMPANYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 10 | `TAXVALUEINDOCUMENTCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 11 | `TAXVALUEINCOMPANYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USACOMPUTEDSALESTAX.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USACOMPUTEDSALESTAX.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND USACOMPUTEDSALESTAX.COUNTERCODE = COUNTER.CODE` |
| `TAX_TAX` | `COMPANYCODE`, `TAXCODE` | [`TAX`](../CORE_MASTER/TAX.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USACOMPUTEDSALESTAX.COMPANYCODE = TAX.COMPANYCODE AND USACOMPUTEDSALESTAX.TAXCODE = TAX.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USACOMPUTEDSALESTAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DOCUMENTTYPE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.TAXCODE,
       t.RATE,
       t.TAXABLEINCOMEINDOCCURRENCY,
       t.TAXABLEINCOMEINCOMPANYCURRENCY,
       t.TAXVALUEINDOCUMENTCURRENCY,
       t.TAXVALUEINCOMPANYCURRENCY
FROM   DB2ADMIN.USACOMPUTEDSALESTAX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
