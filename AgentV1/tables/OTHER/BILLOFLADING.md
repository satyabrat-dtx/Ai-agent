# DB2ADMIN.BILLOFLADING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 135139

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `BILLOFLADINGDATE` | DATE | NOT NULL |  |  |  |
| 4 | `SOURCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `GROSSWEIGHT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 6 | `NETWEIGHT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 7 | `WEIGHINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `TOTALCONTAINERS` | INTEGER | NOT NULL |  |  |  |
| 9 | `TYPEOFSERVICE` | CHAR(25) |  |  |  |  |
| 10 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 11 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `PLACECODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `PRINTDATE` | DATE |  |  |  |  |
| 14 | `ORIGINALBILLOFLADINGNO` | CHAR(25) |  |  |  |  |
| 15 | `ORIGINALBILLOFLADINGDATE` | DATE |  |  |  |  |
| 16 | `SHIPPINGAIRLINENAME` | CHAR(50) |  |  |  |  |
| 17 | `VESSELNO` | CHAR(50) |  |  |  |  |
| 18 | `ETA` | DATE |  |  |  |  |
| 19 | `ETD` | DATE |  |  |  |  |
| 20 | `CONTAINERNO` | CHAR(50) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BILLOFLADING.COMPANYCODE = COMPANY.CODE` |
| `DESTINATION_PLACE` | `COMPANYCODE`, `PLACECODE` | [`DESTINATION`](../CORE_MASTER/DESTINATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BILLOFLADING.COMPANYCODE = DESTINATION.COMPANYCODE AND BILLOFLADING.PLACECODE = DESTINATION.CODE` |
| `UNITOFMEASURE_WEIGHINGUOM` | `WEIGHINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BILLOFLADING.WEIGHINGUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BILLOFLADING_BILLOFLADDINGNO` | [`BANKCERTIFICATE`](../ITEM_MASTER/BANKCERTIFICATE.md) | `COMPANYCODE`, `DIVISIONCODE`, `BILLOFLADDINGNOCODE` | `BANKCERTIFICATE.COMPANYCODE = BILLOFLADING.COMPANYCODE AND BANKCERTIFICATE.DIVISIONCODE = BILLOFLADING.DIVISIONCODE AND BANKCERTIFICATE.BILLOFLADDINGNOCODE = BILLOFLADING.CODE` |
| `BILLOFLADING_DETAIL` | [`BILLOFLADINGDETAIL`](../SALES/BILLOFLADINGDETAIL.md) | `BILLOFLADINGCOMPANYCODE`, `BILLOFLADINGDIVISIONCODE`, `BILLOFLADINGCODE` | `BILLOFLADINGDETAIL.BILLOFLADINGCOMPANYCODE = BILLOFLADING.COMPANYCODE AND BILLOFLADINGDETAIL.BILLOFLADINGDIVISIONCODE = BILLOFLADING.DIVISIONCODE AND BILLOFLADINGDETAIL.BILLOFLADINGCODE = BILLOFLADING.CODE` |
| `BILLOFLADING_AWBNO` | [`COMMERCIALINVOICE`](../CORE_MASTER/COMMERCIALINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `AWBNOCODE` | `COMMERCIALINVOICE.COMPANYCODE = BILLOFLADING.COMPANYCODE AND COMMERCIALINVOICE.DIVISIONCODE = BILLOFLADING.DIVISIONCODE AND COMMERCIALINVOICE.AWBNOCODE = BILLOFLADING.CODE` |

## Indexes

- `BILLOFLADINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.BILLOFLADINGDATE,
       t.SOURCE,
       t.GROSSWEIGHT,
       t.NETWEIGHT,
       t.WEIGHINGUOMCODE,
       t.TOTALCONTAINERS,
       t.TYPEOFSERVICE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE
FROM   DB2ADMIN.BILLOFLADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
