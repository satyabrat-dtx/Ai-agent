# DB2ADMIN.RESERVATIONPLANNINGSTATUS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `RESERVATIONLINE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 214904

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `RESERVATIONLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `PLANUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `USERPRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `PLANUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `USERSECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `PLANUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `USERPACKAGINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `NETTEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `NETTEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `NETTEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `REQUISITIONUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `REQUISITIONUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `REQUISITIONUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `PURCHASEUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `PURCHASEUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `PURCHASEUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `ADDITIONALUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `ADDITIONALUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `ADDITIONALUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 24 | `MODIFIED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `DELETED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `REPLAN` | SMALLINT | NOT NULL |  |  |  |
| 27 | `TRACECREATIONID` | DECIMAL(11,0) |  |  |  |  |
| 28 | `TRACELINE` | INTEGER | NOT NULL |  |  |  |
| 29 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 30 | `PLANRUNNING` | SMALLINT | NOT NULL |  |  |  |
| 31 | `PLANNERANNOTATION` | VARCHAR(250) |  |  |  |  |
| 32 | `LASTPLANNINGTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 33 | `USEBASEQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 34 | `UNLINKED` | SMALLINT | NOT NULL |  |  |  |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RESERVATIONPLANNINGSTATUS.COMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_USERPACKAGINGUOM` | `USERPACKAGINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RESERVATIONPLANNINGSTATUS.USERPACKAGINGUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERPRIMARYUOM` | `USERPRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RESERVATIONPLANNINGSTATUS.USERPRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERSECONDARYUOM` | `USERSECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RESERVATIONPLANNINGSTATUS.USERSECONDARYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RESERVATIONPLANNINGSTATUSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.RESERVATIONLINE,
       t.PLANUSERPRIMARYQUANTITY,
       t.USERPRIMARYUOMCODE,
       t.PLANUSERSECONDARYQUANTITY,
       t.USERSECONDARYUOMCODE,
       t.PLANUSERPACKAGINGQUANTITY,
       t.USERPACKAGINGUOMCODE,
       t.NETTEDUSERPRIMARYQUANTITY
FROM   DB2ADMIN.RESERVATIONPLANNINGSTATUS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
