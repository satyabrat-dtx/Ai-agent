# DB2ADMIN.PURCHASEORDERIE

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134110

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 5 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `ORDERTYPEE` | INTEGER | NOT NULL |  |  |  |
| 7 | `DDPAYABLEAT` | CHAR(30) |  |  |  |  |
| 8 | `DDCHARGESPAYBYE` | INTEGER | NOT NULL |  |  |  |
| 9 | `SCHEMETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 15 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `PLANTINVOICECODE` | CHAR(15) |  | FK | foreign_key |  |
| 17 | `SELECTIONDATE` | DATE |  |  |  |  |
| 18 | `EXCISEINCLUSIVE` | CHAR(3) |  |  |  |  |
| 19 | `ADVANCEOPTION` | INTEGER | NOT NULL |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `ORDERPARTNERSUPPLYSTATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PURCHASEORDERIE.COMPANYCODE = COMPANY.CODE` |
| `PLANTINVOICE_PLANTINVOICE` | `COMPANYCODE`, `PLANTINVOICEDIVISIONCODE`, `PLANTINVOICECODE` | [`PLANTINVOICE`](../CORE_MASTER/PLANTINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PURCHASEORDERIE.COMPANYCODE = PLANTINVOICE.COMPANYCODE AND PURCHASEORDERIE.PLANTINVOICEDIVISIONCODE = PLANTINVOICE.DIVISIONCODE AND PURCHASEORDERIE.PLANTINVOICECODE = PLANTINVOICE.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERIE.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND PURCHASEORDERIE.SCHEMETYPECODE = SCHEMETYPE.CODE` |
| `STATE_ORDERPARTNERSUPPLYSTATE` | `ORDERPARTNERSUPPLYSTATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `PURCHASEORDERIE.ORDERPARTNERSUPPLYSTATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.ORDERTYPEE,
       t.DDPAYABLEAT,
       t.DDCHARGESPAYBYE,
       t.SCHEMETYPECODE,
       t.BASICVALUE,
       t.GROSSVALUE
FROM   DB2ADMIN.PURCHASEORDERIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
