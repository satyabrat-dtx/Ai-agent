# DB2ADMIN.TREPURCHASEORDEREVENTFLOW

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `PURCHASEORDERTEMPLATECODE`, `EVENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69338

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PURCHASEORDERTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EVENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TREPURCHASEORDEREVENTFLOW.COMPANYCODE = COMPANY.CODE` |
| `PURCHASEORDERTEMPLATE_PURCHASEORDERTEMPLATE` | `COMPANYCODE`, `PURCHASEORDERTEMPLATECODE` | [`PURCHASEORDERTEMPLATE`](../PURCHASING/PURCHASEORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREPURCHASEORDEREVENTFLOW.COMPANYCODE = PURCHASEORDERTEMPLATE.COMPANYCODE AND TREPURCHASEORDEREVENTFLOW.PURCHASEORDERTEMPLATECODE = PURCHASEORDERTEMPLATE.CODE` |
| `TREPURCHASEORDEREVENT_EVENT` | `COMPANYCODE`, `EVENTCODE` | [`TREPURCHASEORDEREVENT`](../PURCHASING/TREPURCHASEORDEREVENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREPURCHASEORDEREVENTFLOW.COMPANYCODE = TREPURCHASEORDEREVENT.COMPANYCODE AND TREPURCHASEORDEREVENTFLOW.EVENTCODE = TREPURCHASEORDEREVENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREPURCHASEORDEREVENTFLOWUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PURCHASEORDERTEMPLATECODE,
       t.EVENTCODE,
       t.SEQUENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TREPURCHASEORDEREVENTFLOW t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
