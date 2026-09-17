# DB2ADMIN.DELIVERYPLANNINGSTATUS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`, `DELIVERYLINE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 66037

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `PLANUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `USERPRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `PLANUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `USERSECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `PLANUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `USERPACKAGINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `NETTEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `NETTEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `NETTEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `REQUISITIONUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `REQUISITIONUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `REQUISITIONUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 20 | `MODIFIED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `DELETED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `REPLAN` | SMALLINT | NOT NULL |  |  |  |
| 23 | `TRACECREATIONID` | DECIMAL(11,0) |  |  |  |  |
| 24 | `TRACELINE` | INTEGER | NOT NULL |  |  |  |
| 25 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 26 | `PLANRUNNING` | SMALLINT | NOT NULL |  |  |  |
| 27 | `PLANNERANNOTATION` | VARCHAR(250) |  |  |  |  |
| 28 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 29 | `LASTPLANNINGTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 30 | `USEBASEQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `PURCHASEUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `PURCHASEUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `PURCHASEUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `ADDITIONALUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `ADDITIONALUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `ADDITIONALUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `UNLINKED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DELIVERYPLANNINGSTATUS.COMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_USERPACKAGINGUOM` | `USERPACKAGINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `DELIVERYPLANNINGSTATUS.USERPACKAGINGUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERPRIMARYUOM` | `USERPRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `DELIVERYPLANNINGSTATUS.USERPRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERSECONDARYUOM` | `USERSECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `DELIVERYPLANNINGSTATUS.USERSECONDARYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DELIVERYPLANNINGSTATUSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.DELIVERYLINE,
       t.PLANUSERPRIMARYQUANTITY,
       t.USERPRIMARYUOMCODE,
       t.PLANUSERSECONDARYQUANTITY,
       t.USERSECONDARYUOMCODE,
       t.PLANUSERPACKAGINGQUANTITY
FROM   DB2ADMIN.DELIVERYPLANNINGSTATUS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
