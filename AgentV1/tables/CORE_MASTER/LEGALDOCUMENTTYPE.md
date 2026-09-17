# DB2ADMIN.LEGALDOCUMENTTYPE

- **Module**: `CORE_MASTER` (low confidence — referenced across 4 modules, so shared reference data)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 6 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111119

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `SELFINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `USEWITHSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 14 | `USEWITHINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `USEWITHCREDITNOTE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEGALDOCUMENTTYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | [`INTERNALORDERTEMPLATE`](../INTERNAL_ORDERS/INTERNALORDERTEMPLATE.md) | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | `INTERNALORDERTEMPLATE.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND INTERNALORDERTEMPLATE.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | [`INTERNALRETURNTEMPLATE`](../INTERNAL_ORDERS/INTERNALRETURNTEMPLATE.md) | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | `INTERNALRETURNTEMPLATE.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND INTERNALRETURNTEMPLATE.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | [`RETURNTEMPLATE`](../INVENTORY/RETURNTEMPLATE.md) | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | `RETURNTEMPLATE.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND RETURNTEMPLATE.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | `SALESDOCUMENT.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND SALESDOCUMENT.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | `SALESORDERTEMPLATE.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND SALESORDERTEMPLATE.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `LEGALDOCUMENTTYPECODE` | `EINVOICEBODY.EINVOICEHEADERCOMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND EINVOICEBODY.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |

## Indexes

- `LEGALDOCUMENTTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.LEGALDOCUMENTTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
