# DB2ADMIN.PROOFOFEXPORT

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 55
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142257

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `PROOFOFEXPORTDATE` | DATE | NOT NULL |  |  |  |
| 4 | `BASEDON` | CHAR(3) |  |  |  |  |
| 5 | `AR4CODE` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `AR4EXCISEYEARREGNO` | CHAR(30) |  | FK | foreign_key |  |
| 7 | `AR4EXCISEYEARCODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `AR4DATE` | DATE |  |  |  |  |
| 9 | `AR3CODE` | CHAR(20) |  | FK | foreign_key |  |
| 10 | `AR3EXCISEYEARREGNO` | CHAR(30) |  | FK | foreign_key |  |
| 11 | `AR3EXCISEYEARCODE` | CHAR(4) |  | FK | foreign_key |  |
| 12 | `AR3DATE` | DATE |  |  |  |  |
| 13 | `FACTORYCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `FACTORYCODE` | CHAR(8) |  | FK | foreign_key |  |
| 15 | `EXPORTBONDNO` | CHAR(30) |  |  |  |  |
| 16 | `EXPORTBONDDATE` | DATE |  |  |  |  |
| 17 | `PLANTINVOICECODE` | CHAR(15) |  | FK | foreign_key |  |
| 18 | `POEACCEPTANCEDATE` | DATE |  |  |  |  |
| 19 | `LETTERNO` | CHAR(30) |  |  |  |  |
| 20 | `LETTERDATE` | DATE |  |  |  |  |
| 21 | `MARITIMENO` | CHAR(30) |  |  |  |  |
| 22 | `MARITIMEDATE` | DATE |  |  |  |  |
| 23 | `AR4PRESENTATIONDATE` | DATE |  |  |  |  |
| 24 | `AR3PRESENTATIONDATE` | DATE |  |  |  |  |
| 25 | `AR4RECEIPTDATE` | DATE |  |  |  |  |
| 26 | `AR3RECEIPTDATE` | DATE |  |  |  |  |
| 27 | `ARE3RECEIVED` | SMALLINT | NOT NULL |  |  |  |
| 28 | `ARE1RECEIVED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `SHIPPINGBILL` | SMALLINT | NOT NULL |  |  |  |
| 30 | `BILLOFLADINGYN` | SMALLINT | NOT NULL |  |  |  |
| 31 | `AWB` | SMALLINT | NOT NULL |  |  |  |
| 32 | `LR` | SMALLINT | NOT NULL |  |  |  |
| 33 | `SHIPMENTCERTIFICATE` | SMALLINT | NOT NULL |  |  |  |
| 34 | `MATERECEIPT` | SMALLINT | NOT NULL |  |  |  |
| 35 | `BRC` | SMALLINT | NOT NULL |  |  |  |
| 36 | `ARE3RECEIVEDDATE` | DATE |  |  |  |  |
| 37 | `ARE1RECEIVEDDATE` | DATE |  |  |  |  |
| 38 | `SHIPPINGBILLDATE` | DATE |  |  |  |  |
| 39 | `BILLOFLADINGYNDATE` | DATE |  |  |  |  |
| 40 | `AWBDATE` | DATE |  |  |  |  |
| 41 | `LRDATE` | DATE |  |  |  |  |
| 42 | `SHIPMENTCERTIFICATEDATE` | DATE |  |  |  |  |
| 43 | `MATERECEIPTDATE` | DATE |  |  |  |  |
| 44 | `BRCDATE` | DATE |  |  |  |  |
| 45 | `SHORTSHIPMENT` | INTEGER | NOT NULL |  |  |  |
| 46 | `SHIPPINGMARKS1` | VARCHAR(100) |  |  |  |  |
| 47 | `PROOFOFEXPORTCOMPLETE` | INTEGER | NOT NULL |  |  |  |
| 48 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 49 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 50 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 51 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 52 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 53 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 54 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AR3_AR3` | `COMPANYCODE`, `DIVISIONCODE`, `AR3CODE`, `AR3EXCISEYEARREGNO`, `AR3EXCISEYEARCODE` | [`AR3`](../SALES/AR3.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | RESTRICT | `PROOFOFEXPORT.COMPANYCODE = AR3.COMPANYCODE AND PROOFOFEXPORT.DIVISIONCODE = AR3.DIVISIONCODE AND PROOFOFEXPORT.AR3CODE = AR3.CODE AND PROOFOFEXPORT.AR3EXCISEYEARREGNO = AR3.EXCISEYEARREGNO AND PROOFOFEXPORT.AR3EXCISEYEARCODE = AR3.EXCISEYEARCODE` |
| `AR4_AR4` | `COMPANYCODE`, `DIVISIONCODE`, `AR4CODE`, `AR4EXCISEYEARREGNO`, `AR4EXCISEYEARCODE` | [`AR4`](../SALES/AR4.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | RESTRICT | `PROOFOFEXPORT.COMPANYCODE = AR4.COMPANYCODE AND PROOFOFEXPORT.DIVISIONCODE = AR4.DIVISIONCODE AND PROOFOFEXPORT.AR4CODE = AR4.CODE AND PROOFOFEXPORT.AR4EXCISEYEARREGNO = AR4.EXCISEYEARREGNO AND PROOFOFEXPORT.AR4EXCISEYEARCODE = AR4.EXCISEYEARCODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PROOFOFEXPORT.COMPANYCODE = COMPANY.CODE` |
| `PLANTINVOICE_PLANTINVOICE` | `COMPANYCODE`, `DIVISIONCODE`, `PLANTINVOICECODE` | [`PLANTINVOICE`](../CORE_MASTER/PLANTINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PROOFOFEXPORT.COMPANYCODE = PLANTINVOICE.COMPANYCODE AND PROOFOFEXPORT.DIVISIONCODE = PLANTINVOICE.DIVISIONCODE AND PROOFOFEXPORT.PLANTINVOICECODE = PLANTINVOICE.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROOFOFEXPORT.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND PROOFOFEXPORT.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PROOFOFEXPORT_PROOFOFEXPORT` | [`AR3`](../SALES/AR3.md) | `COMPANYCODE`, `DIVISIONCODE`, `PROOFOFEXPORTCODE` | `AR3.COMPANYCODE = PROOFOFEXPORT.COMPANYCODE AND AR3.DIVISIONCODE = PROOFOFEXPORT.DIVISIONCODE AND AR3.PROOFOFEXPORTCODE = PROOFOFEXPORT.CODE` |
| `PROOFOFEXPORT_PROOFOFEXPORT` | [`AR4`](../SALES/AR4.md) | `COMPANYCODE`, `DIVISIONCODE`, `PROOFOFEXPORTCODE` | `AR4.COMPANYCODE = PROOFOFEXPORT.COMPANYCODE AND AR4.DIVISIONCODE = PROOFOFEXPORT.DIVISIONCODE AND AR4.PROOFOFEXPORTCODE = PROOFOFEXPORT.CODE` |

## Indexes

- `PROOFOFEXPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.PROOFOFEXPORTDATE,
       t.BASEDON,
       t.AR4CODE,
       t.AR4EXCISEYEARREGNO,
       t.AR4EXCISEYEARCODE,
       t.AR4DATE,
       t.AR3CODE,
       t.AR3EXCISEYEARREGNO,
       t.AR3EXCISEYEARCODE
FROM   DB2ADMIN.PROOFOFEXPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
